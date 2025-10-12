#ifndef LIFE_H
#define LIFE_H

/* Macros for accessing and modifying cell states */
#define CELL(I,J) (field[size*(I)+(J)])
#define ALIVE(I,J) t[size*(I)+(J)] = 1
#define DEAD(I,J)  t[size*(I)+(J)] = 0

/* Function prototypes */
int count_alive(const char *field, int i, int j, int size);
void evolve(const char *field, char *t, int size);

#endif /* LIFE_H */
