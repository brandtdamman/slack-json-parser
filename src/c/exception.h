#ifndef EXCEPTION_HEADER
#define EXCEPTION_HEADER

// Denoted enums with _e at end to differentiate from type/variable name.
typedef enum exception_types {
    INFO,
    WARNING,
    ERROR,
    CRITICAL
} exception_types_e;

// TODO: Finalize prototypes.
void exception_handling(int type, char* msg);
int is_log_present();
void critical_error(char* msg);
void set_verbose(int verbosity);

#endif