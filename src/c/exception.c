/**
* Exception Handling file for Slack JSON Parser.  Centralizes all error
* output and log creation.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "exception.h"

// VERBOSE TAG
int verbose = 0;

/**
 * General handling function which passes information to the respective functions.
 * 
 * @param type The type of exception
 * @param msg Message of the exception
 */
void exception_handling(int type, char* msg) {
    // Don't bother outputting anything if it is only INFO-level
    // and not verbose.
    if (type == INFO && verbose) {
        return;
    }

    // Creating message prefix
    char* fullMsg = malloc(sizeof(char) * (strlen(msg) + 10));
    switch (type) {
        case INFO:
            strcat(fullMsg, "[INFO]:  ");
            break;
        case WARNING:
            strcat(fullMsg, "[WARN]:  ");
            break;
        case ERROR:
            strcat(fullMsg, "[ERROR]: ");
            break;
        case CRITICAL:
            // Specialty case.  Needs to abort.
            critical_error(msg);
            break;
    }

    // Add exception message to final message.
    strcat(fullMsg, msg);
    strcat(fullMsg, "\n");

    if (verbose) {
        FILE* fp;
        // Perform log check.
        if (is_log_present()) {
            // APPEND
            fp = fopen("slackjp-out.log", "a+");
        } else {
            fp = fopen("slackjp-out.log", "w");
        }

        // Print to log file if verbose.
        fputs(fullMsg, fp);
    }

    // Print to console.
    printf("%s", fullMsg);
}

/**
 * Confirms if there is a log in the current directory.
 * 
 * @return 1 if log is present, otherwise 0
 */
int is_log_present() {
    return access("slackjp-out.log", F_OK) + 1;
}

/**
 * Worst case circumstance for the program.  Returns a 400-series
 * exit status to I/O.
 * 
 * @param msg technical details for critical error
 */
void critical_error(char* msg) {
    // TODO: Add critical error components.
}

/**
 * Sets the verbose flag to the given value.
 * 
 * @param verbosity 1 for verbose, otherwise 0
 */
void set_verbose(int verbosity) {
    verbose = verbosity;
}