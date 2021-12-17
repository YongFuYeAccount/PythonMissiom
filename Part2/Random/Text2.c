# include <stdio.h>
void main( )
{ int s=0,m=0,n=0;
int y;
while(1)
{ 
  int y=256,m=16,n=16;
	  scanf("%x",&y);
      m=y/16; 
      n=y%16;
    switch(m)  {  
				case 1:m=0; break;
				case 2:m=1; break;
				case 3:m=2; break;
				case 4:m=3; break;
	            case 5:m=4; break;
				case 6:m=5; break;
	            case 7:m=6; break;
				case 8:m=7; break;
	            case 9:m=8; break;
				case 10:m=9; break;
	            case 11:m=10; break;
				case 12:m=11; break;
	            case 13:m=12; break;
				case 14:m=13; break;
            	case 15:m=14; break;
				case 16: m=15; break;
			break;
  }

  switch (n) {  
              case 1:{n=0;s+=y; s=s%256;}; break;
			  case 2:{n=1;s+=y;s=s%256;}; break;
			  case 3:{n=2;s+=y;s=s%256;}; break;
			  case 4:{n=3;s+=y; s=s%256;}; break;
			  case 5:{n=4;s+=y;s=s%256;}; break;
			  case 6:{n=5;s+=y; s=s%256;}; break;
			  case 7:{n=6;s+=y;s=s%256;}; break;
			  case 8:{n=7;s+=y;s=s%256;}; break;
			  case 9:{n=8;s+=y;s=s%256;}; break;
			  case 10:{n=9;s+=y;s=s%256;}; break;
			  case 11:{n=10;s+=y;s=s%256;}; break;
			  case 12: {n=11;s+=y;s=s%256;}; break;
			  case 13:{n=12;s+=y; s=s%256;}; break;
			  case 14: {n=13;s+=y;s=s%256;}; break;
			  case 15:{n=14;s+=y;s=s%256;}; break;
			  case 16: {n=15;s+=y;s=s%256;}; break;
				  break;
  } 
  if(y==256)
			printf(" ‰»Î¥ÌŒÛ");
  if(n==16)
	  printf(" ‰»Î¥ÌŒÛ");
  if(m==16)
        printf(" ‰»Î¥ÌŒÛ");
   if(getchar()=='\n')break;	   
 }
 printf("sum=%x\n",s); 
  system("pause");
}