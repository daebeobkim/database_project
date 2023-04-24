#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRA = 0x07;

	while (1)
	{

		// 두 번째
		PORTA = 0x06;
		_delay_ms(1000);
		PORTA = 0x03;
		_delay_ms(1000);
		PORTA = 0x01;
		_delay_ms(1000);
	}
}
