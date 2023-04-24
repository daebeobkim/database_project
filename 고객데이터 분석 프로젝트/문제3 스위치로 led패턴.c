#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	char pattern = 0x01;
	char state_previous = 0, state_current;
	DDRA = 0x07;
	DDRC = 0x00;
	PORTD = pattern;
	while (1)
	{
		state_current = PINC&0x08;
		if(state_current == 0x00 && state_previous == 0x08)
		{
			pattern <<= 1;
			pattern |= 0x01;    
			if(pattern == 0x0F) pattern = 0x01;   
			PORTA = pattern;
		}
		state_previous = state_current;
	}
}
