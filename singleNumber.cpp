#include <iostream>

int singleNumber(int A[], int n) {
	int result = 0;
	for (int i = 0; i < n; ++i) {
		result = result ^ A[i];
	}
	return result;
};

using namespace std;
int main(int argc, char *argv[]) {
	int array[9] = {5, 5, 6, 6, 7, 7, 8, 8, 9};
	printf("%d", singleNumber(array, 9));
}