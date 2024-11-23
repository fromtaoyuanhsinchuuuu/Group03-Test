#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LEN 100
#define MAX_LINE_LEN 256

int get_file_info(FILE *fp, int *file_length, int *first_line_length, int *data_line_length, int *last_line_length) {
    if (fp == NULL) {
        return -1;
    }

    // 取得檔案總長度
    fseek(fp, 0, SEEK_END);
    int file_size = ftell(fp);
    *file_length = file_size;
    if (*file_length == -1L) {
        return -1;
    }

    // 讀取第一行
    fseek(fp, 0, SEEK_SET);
    char buffer[MAX_LINE_LEN];
    fgets(buffer, sizeof(buffer), fp);
    *first_line_length = strlen(buffer);

    // 讀取第二行（第一個資料行）
    fgets(buffer, sizeof(buffer), fp);
    *data_line_length = strlen(buffer);

    // 讀取最後一行的長度
    // 先跳到檔案尾端
    fseek(fp, -1, SEEK_END);

    long pos = ftell(fp);
    char c = fgetc(fp);
    int len = 1;
    while (c != 'N') {
        pos--;
        len++;
        fseek(fp, pos, SEEK_SET);
        c = fgetc(fp);
    }
    *last_line_length = len;

    return 0;
}

int main(){
    int n, q;
    
    // 讀取 n 和 q
    scanf("%d %d", &n, &q);

    // 動態分配 n 個檔案名稱的記憶體
    char **filenames = (char **)malloc(n * sizeof(char *));
    for(int i = 0; i < n; i++) {
        filenames[i] = (char *)malloc(MAX_FILENAME_LEN * sizeof(char));
        scanf("%s", filenames[i]);
    }

    int count_no_change = 0; // 記錄不影響雜湊值的指令數

    // 執行 q 次指令
    for(int cmd = 0; cmd < q; cmd++) {
        int x, y;
        unsigned int z;
        scanf("%d %d %u", &x, &y, &z);
        FILE *fp = fopen(filenames[x-1], "r+");
        int file_size, P_len, D_len, N_len;
        if (get_file_info(fp, &file_size, &P_len, &D_len, &N_len) != 0) {
            printf("error in get block %d\n", x);
        }

        // 計算 s
        int k_plus_1 = ((file_size - P_len - N_len) / D_len) + 1;
        int total_shifts = (k_plus_1-1) / 25;
        int shifts_before = (y-1) / 25;
        int s = total_shifts - shifts_before;

        // 計算 data y 行的位元組偏移量
        // Offset = first_line_length + (y -1) * data_line_length
        long data_y_offset = P_len + (y - 1) * D_len;
        fseek(fp, data_y_offset, SEEK_SET);

        // 讀取原始的 data_y
        unsigned int original_data;
        // 假設資料行格式為 "y: <data>"
        // 先讀取整行，再提取數值
        char data_line[MAX_LINE_LEN];
        fgets(data_line, sizeof(data_line), fp);
        sscanf(data_line, "%u", &original_data);

        // 修改 data y 行為 z
        // 跳轉回 data y 行的起始位置
        fseek(fp, data_y_offset, SEEK_SET);
        fprintf(fp, "%u\n", z);
        
        if (s > 30) {
            count_no_change++;
            fclose(fp);
            continue;
        }
        // 計算 new_nonce
        unsigned int new_nonce;
        // 計算 nonce 行的位元組偏移量
        long nonce_offset = P_len + (k_plus_1-1) * D_len;
        fseek(fp, nonce_offset, SEEK_SET);

        // 讀取 current_nonce
        unsigned int current_nonce;
        char nonce_line[MAX_LINE_LEN];
        fgets(nonce_line, sizeof(nonce_line), fp);
        sscanf(nonce_line, "N: %u", &current_nonce);

        // 計算 new_nonce = current_nonce XOR (data_y << s) XOR (z << s)
        new_nonce = current_nonce ^ ((original_data << s) & 0x3FFFFFFF) ^ ((z << s) & 0x3FFFFFFF);

        // 判斷 nonce 是否改變
        if(new_nonce == current_nonce){
            count_no_change++;
        }
        else{
            // 更新 nonce
            // 跳轉回 nonce 行的起始位置
            fseek(fp, nonce_offset, SEEK_SET);
            char buf[MAX_LINE_LEN];
            memset(buf, '\0', N_len);
            fwrite(buf, 1, N_len, fp);
            fseek(fp, nonce_offset, SEEK_SET);
            fprintf(fp, "N: %u\n", new_nonce);
        }

        fclose(fp);
    }

    // 釋放所有動態分配的記憶體
    for(int i = 0; i < n; i++) {
        free(filenames[i]);
    }
    free(filenames);

    // 輸出不影響雜湊值的指令數
    printf("%d\n", count_no_change);

    return 0;
}
