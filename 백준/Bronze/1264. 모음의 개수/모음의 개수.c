#include <stdio.h>
#include <string.h>

int count(char *sentence) {
	char vowel[] = "aeiouAEIOU";
	int count = 0;

	for (int i = 0; i < strlen(sentence); i++) {
		for (int j = 0; j < strlen(vowel); j++) {
			if (sentence[i] == vowel[j]) {
				count++;
				break;
			}
		}
	}

	return count;
}

int main() {
	char sentence[1000][257];
	int line = 0;

	while (1) {
		fgets(sentence[line], sizeof(sentence[line]), stdin);

		if (sentence[line][0] == '#' && sentence[line][1] == '\n') {
			break;
		}

		line++;
	}

	for (int i = 0; i < line; i++) {
		int result = count(sentence[i]);
		printf("%d\n", result);
	}

	return 0;
}