#include <stdio.h>
#include <string.h>

 #define MAX_BOOK_COUNT  5

struct book{
    char name[25];
    char dayofissue[10];
    char returnday[10];
};

int main(){
  struct book books[MAX_BOOK_COUNT];
  int bookcount = 0;
  char continuebook = 'y';

  while(continuebook == 'y'|| continuebook =='Y'){
    if(bookcount >= MAX_BOOK_COUNT){
        printf("\nYou have reached the maximum input");
        break;
    }
  printf("\nEnter book name: ");
  fgets(books[bookcount].name,25,stdin);

  printf("\nEnter book issued day: ");
  scanf("%s",&books[bookcount].dayofissue);



  printf("\nEnter book returned day: ");
  scanf("%s",&books[bookcount].returnday);

  

 bookcount++;
 scanf("%c");
 printf("\nDo you want to continue(y/n): ");
 scanf("%c",&continuebook);
}

   printf("\n******************************\n");
   printf("\tLIBRARY");
   printf("\n******************************\n");

 for(int i = 0; i < bookcount; i++){
  
    printf("\nBOOK NAME: %s",books[i].name);
    printf("\nBOOK ISSUED DAY: %s",books[i].dayofissue);
    printf("\nBOOK RETURNED DAY: %s",books[i].returnday);
 }  
 printf("\nTOTAL NO.OF BOOKS: %d",bookcount);

    return 0;
}