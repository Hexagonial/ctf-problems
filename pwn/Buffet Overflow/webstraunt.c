#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>

char* pathToFlag = "/flag.txt";

int main() {
    runRestaurant();
    return 0;
}

void runRestaurant() {
    char order[64];
    char payment[16];
    printf("Welcome to the grand opening of the webstraunt!\nPlease input your order. Here is the menu:\n");
    printf("1. Digital Fries\n2. Spaghetti Strings\n3. Bacon Bits\n4. PIE\n>>> ");
    fflush(stdout);

    gets(order);

    printf("\nAlright! You are trying to order:\n");
    printf(order);
    printf("\n\nPlease enter your payment information.\n>>> ");
    fflush(stdout);

    gets(payment);

    printf("\n\nThank you for your order! It will arrive within 4-900 days\n");
    fflush(stdout);
}

void secretMenu() {
    char flag[100];
    int fd = open(pathToFlag, O_RDONLY);
    if (fd < 0) {
    	printf("Error opening flag file. errno: %d\n", errno);
    }
    read(fd, flag, 100);
    printf("\nWelcome to the secret menu! We only have one item at the moment:\n1. ");
    printf(flag);
    fflush(stdout);
}
