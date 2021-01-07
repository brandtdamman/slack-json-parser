/*
* 
*  ____  _            _          _ ____   ___  _   _   ____                          
* / ___|| | __ _  ___| | __     | / ___| / _ \| \ | | |  _ \ __ _ _ __ ___  ___ _ __ 
* \___ \| |/ _` |/ __| |/ /  _  | \___ \| | | |  \| | | |_) / _` | '__/ __|/ _ \ '__|
*  ___) | | (_| | (__|   <  | |_| |___) | |_| | |\  | |  __/ (_| | |  \__ \  __/ |   
* |____/|_|\__,_|\___|_|\_\  \___/|____/ \___/|_| \_| |_|   \__,_|_|  |___/\___|_|   
*                                                                                   
* Copyright 2021, Brandt Damman
* Slack is a software application developed by Slack Technologies, Inc.  All rights reserved.
*
*/

// SYSTEM Libraries
// #include <fcntl.h>
// #include <pthread.h>
// #include <semaphore.h>
#include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include <sys/wait.h>
// #include <unistd.h>

// SJP Classes/Libraries
#include "commands.h"
#include "exception.h"

#include "slackjp.h"

//sem_t fileLock;

int main(int argc, char *argv[]) {
    // Pre-process check.
    if (argc == 1) {
        // TODO: Change to CRITICAL.
        exception_handling(ERROR, "Invalid number of arguments.");
        return -1;
    }

    // sem_init(&fileLock, 0, 1);

    // int threadCount = 5;
    // pthread_t* threads = (pthread_t*)malloc(sizeof(pthread_t) * threadCount);

    help_screen();

    // printf("Number of arguments: %d\n", argc);
    // int i;
    // for (i = 0; i < argc; i++) {
    //     printf("Argument %d, %s\n", i, argv[i]);
    // }

    return 0;
}