#include <iostream>

int** FillArray(int n) {
    int** arr = new int* [n];

    for (int i = 0; i < n; ++i) {
        arr[i] = new int[n];
        for (int j = 0; j < n; ++j) {
            std::cin >> arr[i][j];
        }
    }

    return arr;
}

int sumAboveSecDiag(int** array, int n) {
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i < n - j - 1) {
                sum += array[i][j];
            }
        }
    }
    return sum;
}

int sumOfSecDiag(int** array, int n) {
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += array[i][n - i - 1];
    }
    return sum;
}

int Max(int** array, int n) {
    int maxElement = array[0][0];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (array[i][j] > maxElement) {
                maxElement = array[i][j];
            }
        }
    }
    return maxElement;
}

int main() {
    int n;
    std::cin >> n;

    int** array = FillArray(n);

    int sumAboveSec = sumAboveSecDiag(array, n);
    int sumOfSec = sumOfSecDiag(array, n);
    int result = sumAboveSec - sumOfSec;

    std::cout << result << " ";

    int maxElement = Max(array, n);
    std::cout << maxElement << std::endl;

    for (int i = 0; i < n; ++i) {
        delete[] array[i];
    }
    delete[] array;

    return 0;
}