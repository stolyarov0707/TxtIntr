#include <iostream>
#include <string>
#include <vector>
#include <unistd.h>
#include <getopt.h>
#include <cmath>

using namespace std;

double asin_operation(vector<double> operands) {
    return asin(operands[0]);
}

double acos_operation(vector<double> operands) {
    return acos(operands[0]);
}

void printHelp() {
cout « "Использование: calculator -o операция [операнды]" « endl;
cout « "Опции:" « endl;
cout « " -o операция задаёт операцию (asin, или acos)" « endl;
cout « " -p вывести справку" « endl;
cout « "Операнды:" « endl;
cout « " От трёх до пяти операндов" « endl;
}

int main(int argc, char* argv[]) {
int option;
string operation;
vector<double> operands;

while ((option = getopt(argc, argv, "o:p")) != -1) {
switch (option) {
case 'o':
operation = optarg;
break;
case 'p':
printHelp();
return 0;
}
}

for (int i = optind; i < argc; ++i) {
double operand = stod(argv[i]);
operands.push_back(operand);
}

if (operation.empty() || operands.size() < 1) {
cout « "Недостаточно параметров" « endl;
return 1;
}
if (operands.size() > 1) {
cout « "Много параметров" « endl;
return 2;
}

double result;

if (operation == "asin") { // Вычисляем арксинус
result = asin_operation(operands);
} else if (operation == "acos") { // Вычисляем арккосинус
result = acos_operation(operands);
} else {
cout « "Неизвестная операция" « endl;
return 3;
}

cout « "Результат: " « result « endl;
return 0;
}
