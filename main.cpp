#include <iostream>
#include "reinas.hpp"
#include "extra_functions.hpp"

int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    al::Reinas r(n);
    r.resolver_backtracking();
    std::cout << exportar_soluciones(r.get_soluciones());
    return 0;
}
