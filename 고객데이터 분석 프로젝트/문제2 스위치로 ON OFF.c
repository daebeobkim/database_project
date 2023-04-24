#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
int main(void)
{
	DDRD = 0x07;
	DDRC = 0x00;
	while (1)
	{
		if((PINC&0x0F) == 0x0E) PORTA = 0x01;
		if((PINC&0x0F) == 0x0D) PORTA = 0x02;
		if((PINC&0x0F) == 0x0B) PORTA = 0x03;
		if((PINC&0x0F) == 0x07) PORTA = 0x04;
		else{
			PORTA = 0x00;
		}
	}
}
