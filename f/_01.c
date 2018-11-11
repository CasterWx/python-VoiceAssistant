#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include <windows.h>
void gotoxy(int x, int y)
{
	COORD pos = {x,y};
	HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleCursorPosition(hOut, pos);
}

void Delay(unsigned int nDelay)
{
    unsigned int i, j, k;
    for (i = 0; i < nDelay; i++)
        for (j = 0; j < 6144; j++)
            k++;
}
char ascii(int d) {
  switch (d) {
  case 1:
    return '1';
    break;
  case 2:
    return '2';
    break;
  case 3:
    return '3';
    break;
  case 4:
    return '4';
    break;
  case 5:
    return '5';
    break;
  case 6:
    return '6';
    break;
  case 7:
    return '7';
    break;
  case 8:
    return '8';
    break;
  case 9:
    return '9';
    break;
  case 0:
    return '0';
    break;}}
void shu(unsigned int j, char *h) {
  int ge, shi, bai, qian;
  ge = j % 10;
  shi = j / 10 % 10;
  bai = j / 100 % 10;
  qian = j / 1000 % 10;
  ge = ascii(ge);
  shi = ascii(shi);
  bai = ascii(bai);
  qian = ascii(qian);
  if (qian != 48) {     h[0] = qian;
    h[1] = bai;
    h[2] = shi;
    h[3] = ge;
  } else if (bai != 48) {
    h[0] = bai;
    h[1] = shi;
    h[2] = ge;
  } else if (shi != 48) {
    h[0] = shi;
    h[1] = ge;
  } else if (ge != 48) {
    h[0] = ge;}}
int main( ) {
	system("0.mp3");
  unsigned int i;
  char k[104] = { 0 };
  for (i = 1; i < 6574; i++){
    char j[6] = { 0 };
    char j1[10] = { '_' };
    shu(i, j);
    strcat(j1, j);
    strcat(j1, ".txt");
    FILE *p;
    if ((p = fopen(j1, "r")) == NULL){
		printf("  ");
		exit(0);}
    gotoxy(0,0);
    while (!feof(p)) {       fgets(k, 103, p);
      printf("%s", k);}
    fclose(p);}
	return 0 ;
}
