#include <stdio.h>

#define MAX_BLOCKS 25
#define MAX_BLOCK_NAME 20
#define MAX_DATA_NUM 5005
#define MAX_LINE_LENGTH 30

unsigned int compute_hash(const int *data, int size) {
    unsigned int h = 0;
    for (int i = 0; i < size; i++) {
        if ((i + 1) % 25 == 0) {
            h = (((h ^ data[i]) << 1) & 0x3FFFFFFF); // 左移 1 位後取模 2^30
        } else {
            h = (h ^ data[i]) & 0x3FFFFFFF; // 僅取低 30 位
        }
    }
    return h;
}

int parse_block_file(const char *filename, unsigned int *previous_hash, int *data, int *nonce, int *data_size) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        fprintf(stderr, "Error opening file: %s\n", filename);
        return -1;
    }

    char line[MAX_LINE_LENGTH];

    while (fgets(line, MAX_LINE_LENGTH, file)) {
        if (line[0] == 'P') {
            sscanf(line, "P: %u", previous_hash); // 解析 previous hash
        } else if (line[0] >= '0' && line[0] <= '9') {
            int value;
            sscanf(line, "%d", &value); // 直接解析數字
            data[*data_size] = value;
            (*data_size)++;
        } else if (line[0] == 'N') {
            sscanf(line, "N: %d", nonce); // 解析 Nonce
        }
    }

    fclose(file);
    return 0;
}

int main() {
    int n, q;
    char filenames[MAX_BLOCKS][MAX_BLOCK_NAME];

    // 讀取輸入
    scanf("%d%d", &n, &q);
    for (int i = 0; i < n; i++) {
        scanf("%s", filenames[i]);
    }

    unsigned int previous_hash = 0;
    for (int i = 0; i < n; i++) {
        unsigned int expected_previous_hash = previous_hash;
        int data[MAX_DATA_NUM], nonce = 0, data_size = 0;

        if (parse_block_file(filenames[i], &previous_hash, data, &nonce, &data_size) == -1) {
            return 1; // 文件讀取失敗
        }

        // 添加 Nonce 作為最後一筆資料
        data[data_size] = nonce;
        data_size++;

        // 計算當前區塊的 hash
        unsigned int current_hash = compute_hash(data, data_size);

        // 比較 hash 值
        if (expected_previous_hash != previous_hash) {
            printf("%d\n", i);
            return 0;
        }

        previous_hash = current_hash;
    }

    // 所有區塊皆正確
    printf("-1\n");
    return 0;
}
