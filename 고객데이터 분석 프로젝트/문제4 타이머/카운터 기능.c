#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

volatile int count = 0;
volatile int state = 0;
volatile int state2 = 0;
volatile int count2 = 0;

ISR(TIMER0_OVF_vect)
{
	count++;
	if (count == 64) {
		count = 0;
		state = !state;
		if (state) PORTC |= (1 << PORTC0);
		else PORTC &= ~(1 << PORTC0);
	}
}

ISR(TIMER2_COMP_vect)
{
	count2++;

	if (count2 == 144) {
		count2 = 0;
		state2 = !state2;
		if (state2) PORTC |= (1 << PORTC1);
		else PORTC &= ~(1 << PORTC1);
	}
}

int main(void)
{
	DDRC |= (1 << DDC0) | (1 << DDC1);
	PORTC &= ~((1 << PORTC0) | (1 << PORTC1));

	TCCR0 |= (1<<CS02) | (1<<CS01) | (1<<CS00);
	TCCR2 |= (1 << CS22) | (0 << CS21) | (1 << CS20);
	TIMSK |= (1 << TOIE0) | (1 << OCIE2);
	OCR0 = 128;
	OCR2 = 71;
	sei();

	while (1) { }

	return 0;
}
