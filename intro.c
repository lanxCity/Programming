#include <stdio.h>

int main(void)
{
    char username[10];
    // Ctr + Alt + m (To stop running task)
    puts("Hello! Welcome to VSCode c programming.");

    printf("Enter your username: ");
    scanf("%s", username);
    printf("Hi %s! Nice to have you onboard...", username);

    return (0);
}