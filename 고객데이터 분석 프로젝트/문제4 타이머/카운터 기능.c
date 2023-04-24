#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

volatile int count = 0;
volatile int state = 0;
volatile int state2 = 0;
volatile int count2 = 0;
ISR(TIMER0_COMP_vect)
{
	count++;
	if(count == 64){
		count = 0;
		state = !state;
		if(state) PORTC = 0x01;
		else PORTC = 0x00;
	}
}
ISR(TIMER2_COMP_vect)
{
	count2++;
	if (count2 == 96) {
		count2 = 0;
		state2 = !state2;
		if (state2) PORTC = 0x03;
		else PORTC = 0x00;
	}
}
int main(void)
{
	DDRC = 0x01;
	PORTC = 0x00;
	TCCR0 |= (1<<WGM01) | (1<<CS02) | (1<<CS01) | (1<<CS00);
	TCCR2 |= (1<<WGM01) | (1<<CS02) | (1<<CS01) | (0<<CS00);
	OCR0 = 128;
	
	TIMSK |= (1<< OCIE0);
	sei();
	while(1){ }
	return 0;
}
