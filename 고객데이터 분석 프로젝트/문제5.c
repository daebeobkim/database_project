#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

int pattern = 0x01;
volatile int state = 0;
volatile int state2 = 0;
volatile int state1 = 0;

ISR(INT0_vect)
{
	state1 = (state + 1) % 2;
}

ISR(INT1_vect)
{
	state2 = (state + 1) % 2;
}

void INIT_PORT(void)
{
	DDRC = 0x01;
	PORTC = 0x00;
	DDRD = 0x00;
}

void INIT_INT0(void)
{
	EIMSK |= (1 << INT0) | (1 << INT1);
	EICRA |= (1 << ISC11) | (1 << ISC01);
	sei();
}

int main(void)
{
	INIT_PORT();
	INIT_INT();


	PORTD = pattern;

	while (1)
	{
		_delay_ms(1000);
		pattern <<= 1;

		if (state1 == 1)
		{
			_delay_ms(5000000000000);
		}

		if (state2 == 1)
		{
			pattern <<= 1;
		}
	}
	return 0;
}
