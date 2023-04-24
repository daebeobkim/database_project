#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

volatile int state = 0;
ISR(INT0_vect)
{
	state = 1;
}
ISR(INT1_vect)
{
	state = 0;
}

void INIT_PORT(void)
{
	DDRC |= 0x07;
	PORTC = 0x00;
	DDRD = 0x00;
}
void INIT_INT0(void)
{
	EIMSK |= (1 << INT0)|(1 << INT1);
	EICRA |= (1<<ISC01)|(1<<ISC11);
	sei();
}

int main(void)
{
	INIT_PORT();
	INIT_INT0();

	int cnt =0;
	char led[]={0x01,0x02,0x04};
	
	while(1){
		if(state == 0){
			PORTC = led[cnt];
			cnt=(cnt+1)%3;
			_delay_ms(300);
		}
		
	}
	return 0;
}
