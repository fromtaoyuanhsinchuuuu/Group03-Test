# 布拉格錢數位帳本-有漏洞？！那我親自來

### 故事 Story
秉持著「做中學」的精神，你在上一個任務中熟悉並理解了布拉格錢數位帳本的運行機制，並從中發現了更多漏洞。你發現了自定義雜湊函數的可計算性，這樣就能在竄改資料的同時改變 Nonce，使得被竄改區塊的雜湊值不變。

你來布拉格、你去布拉格、你征服布拉格錢數位帳本。正好缺大學生活費的你決定以此機會大賺一筆，並且你能做的比上次的駭客更好，不會留下 hash 與 previous hash 不一致的問題。

註：故事中的布拉格為虛構城市，與捷克首都布拉格並無任何關係

註：竄改區塊鏈資料為不良行為，請勿在真實環境中嘗試

Driven by the spirit of "learning by doing," you have familiarized yourself with the operational mechanism of the PragueCoin digital ledger in the previous mission and have discovered more vulnerabilities. You notice that the custom hash function is computable, allowing you to modify the data while altering the Nonce so that the tampered block's hash value remains unchanged.

You come to Prague, you conquer Prague, and you dominate the PragueCoin digital ledger. With a lack of university living expenses, you decide to seize this opportunity to make a fortune. Moreover, you aim to outperform the previous hacker by not leaving hash and previous hash inconsistencies.

Note: The Prague mentioned in this story is a fictional city and has no relation to the capital of the Czech Republic.

Disclaimer: Tampering with blockchain data is unethical. Do not attempt it in a real-world environment.


### 布拉格錢（Block Chain）數位帳本簡介 Introduction to PragueCoin (Blockchain) Digital Ledger
**注意：** 簡介內容與作業有些不同，建議閱讀
![Block_Chain](https://github.com/fromtaoyuanhsinchuuuu/Group03-Test/blob/main/image/Block_Chain.jpeg?raw=true)

一條區塊鏈是由數個區塊(block)組成，每個區塊內容須包含三個部份：前一個區塊的雜湊值(previous hash)、數筆資料(data)、以及特殊數字 Nonce。

previous hash 是形成鏈狀結構的關鍵。在題目中，我們假設 previous hash 是不能被任何人改變的（包括準備竄改資料的你），如何依照區塊鏈特性在不影響區塊雜湊值的情況下更改指定資料會是這題的關鍵。

data 在我們的題目只會以數字的型態存在，以方便計算區塊的雜湊值(hash)，並且我們保證一個區塊至少會有一個 data。

特殊數字 Nonce 並不像前兩者一樣具有紀錄功能。Nonce 是單純用來改變區塊的雜湊值(hash)的數字，在計算區塊雜湊值的時候會被使用。本題希望同學在更改指定資料的同時，適時將區塊的 Nonce 換成合適的數字，使得區塊雜湊值不變。

一個區塊的雜湊值是根據區塊內容及使用的雜湊函數決定的，在此我們將用文字檔案模擬區塊（一個文字檔案代表一個區塊）、並使用自定義的雜湊函數（詳見下方雜湊函數），進行布拉格錢數位帳本的竄改。

**Note:** The introduction content differs slightly from the assignment. Reading is recommended.  

A blockchain consists of several blocks, each containing three parts: the previous block's hash (previous hash), several pieces of data (data), and a special number called Nonce.

The `previous hash` is the key to forming the chain-like structure. In this problem, we assume the `previous hash` cannot be changed by anyone (including you, the one tampering with the data). The challenge is how to modify specified data in a block without affecting the block's hash value, adhering to blockchain characteristics.

The `data` will only exist in numeric form in this problem for ease of computation of the block's hash value. We guarantee that each block will contain at least one piece of data.

The special number `Nonce` does not have a record-keeping function like the first two components. Nonce is purely a number used to change the block's hash value (hash). In this problem, you are required to appropriately adjust the Nonce while modifying specified data to ensure the block's hash value remains unchanged.

A block's hash value is determined by its contents and the hash function used. Here, we simulate blocks with text files (one text file represents one block) and use a custom hash function (described below) to perform the tampering operation on the PragueCoin digital ledger.


### 題目敘述 Problem Description
給定兩數字 $n$ 和 $q$，代表有 $n$ 個區塊檔案 (`block_i_1.txt`, `block_i_2.txt`, ..., `block_i_n.txt`)，及 $q$ 個竄改指令。接著請依照輸入的指令（指令格式詳見下方Input Format）竄改特定區塊的指定資料，並**適時**更改區塊 Nonce，使得區塊雜湊值維持不變。

沒錯，「**適時**更改 Nonce」代表某些情況下竄改操作並不會影響區塊雜湊值，也就不會需要調整 Nonce 來確保雜湊值不變。請紀錄 $q$ 個竄改指令中，有多少指令是執行**不影響雜湊值**的竄改操作，並將紀錄結果輸出。

另外，因為最後一個區塊沒有對應的 previous hash，所以我們的竄改指令不會要求竄改最後一個區塊的資料。

Given two numbers $n$ and $q$, where $n$ represents the number of block files (`block_i_1.txt`, `block_i_2.txt`, ..., `block_i_n.txt`), and $q$ represents the number of tampering commands, modify the specified data in a particular block according to the input commands (command format detailed below). **Adjust the Nonce appropriately** to ensure that the block's hash value remains unchanged.

Yes, "appropriately adjust the Nonce" means that in some cases, tampering operations may not affect the block's hash value, so no Nonce adjustment is needed to ensure the hash value remains the same. Record how many of the $q$ tampering commands resulted in hash values that were unaffected and output the record.

Additionally, since the last block does not have a corresponding `previous hash`, tampering commands will not require modifying the data of the last block.


### 檔案格式 File Format
與作業有所不同，請詳細閱讀。differs from the assignment, please read carefully.

檔名固定為 `block_i_j.txt`，其中 $i$ 為測資的編號， $j$ 為區塊的編號

檔案內容格式如下

File names are fixed as `block_i_j.txt`, where $i$ represents the test case index and $j$ represents the block number.

The file content is formatted as follows:
```
P: <pre-hash>
<data 1>
<data 2>
.
.
<data k>
N: <nonce>
```
- 第一行 P 後面的數字是 previous hash，為上一個區塊的雜湊值
    - 第一個區塊的 P 必為 0
- 最後一行 N 後面的數字是 Nonce，用以計算或改變這個區塊的雜湊值 (詳見下方雜湊函數)
    - 最後一個區塊的 Nonce 必為 0
- 剩下的部份是區塊中的 data，會按照順序排好（如上方範例中 $1\ to\ k$）
    - 我們保證一個區塊至少會有一個 data
- **注意：** 與作業不同的地方有以下兩點
    - data 開頭沒有編號
    - data 這次我們保證同一個檔案(block)的所有 data 都有一樣的位數 (previous hash 與 nonce 的位數可能與 data 位數不同)
    - 這些改動方便同學計算行數（或是offset），並進行 random access
- The first line after `P:` contains the previous hash, which is the hash value of the previous block. 
    - The `previous hash` of the first block is always 0.
- The last line after `N:` contains the Nonce, used to compute or alter the block's hash value (see below for the hash function).
    - The `Nonce` of the last block is always 0.
- The remaining lines contain the block's data, ordered sequentially (`<data 1>` to `<data k>`).
    - We guarantee that each block will contain at least one piece of data.
- **Note:** Differences from the assignment include:
    - Data entries do not have an index prefix.
    - In this version, all data in a single block have the same number of digits (the `previous hash` and `Nonce` may have a different number of digits).
    - These changes make line counting (or offset computation) and random access easier.


### 雜湊函數 (Hash function)
雜湊函數定義如下，將區塊的所有 data 以及 Nonce 進行運算即可得到區塊的雜湊值（不會使用到 previous hash）
- 初始 $H_0=0$
- 依照下列式子反覆運算
    - ![alt text](https://github.com/fromtaoyuanhsinchuuuu/Group03-Test/blob/main/image/Hash_Function.jpg?raw=true)
    - 假設區塊中有 $k$ 個data，則 $i\ from\ 1\ to\ k+1$
    - $d_{k+1}$ 為區塊的 Nonce，其餘 $d_i$ 就是 \<data $i$ \>
- k+1 次運算後， $H_{k+1}$ 就是這個區塊的雜湊值

註： $\oplus$ 代表 XOR、 $\ll$ 代表邏輯左移、 $mod$ 代表取模


The hashing function is defined as follows. Compute the block's hash value by operating on all its `data` entries and the `Nonce`:
- Initial $H_0=0$ .
- Repeatedly compute using the formula:
    - ![alt text](https://github.com/fromtaoyuanhsinchuuuu/Group03-Test/blob/main/image/Hash_Function.jpg?raw=true)
    - Assume the block contains $k$ data entries; iterate $i\ from\ 1\ to\ k+1$ .
    - $d_{k+1}$ represents the block's `Nonce`, while the remaining $d_i$ represents `<data i>`.
- After k+1 computations, $H_{k+1}$ is the hash value of the block.

Note: $\oplus$ denotes XOR, $\ll$ denotes logical left shift, and $mod$ denotes modulus.

### Input Format
第一行只有兩個數字 $n$ 和 $q$（中間以空格隔開），代表有 $n$ 個區塊檔案及 $q$ 個需要竄改的資料

接著 $n$ 行是檔案名稱，block_i_j.txt ( j $from\ 1\ to\ n$ )，我們保證檔名會照順序排好

接者 $q$ 行，每行皆有三個數字 $x, y, z$（中間以空格隔開），請將 block_i_x.txt 中的 \<data y> 改成 z

**我們保證原先的 \<data y> 與數字 z 有相同的位數，請直接覆蓋資料，不必擔心會有多出/缺少的位數導致需要平移檔案內容的狀況。**

**Nonce 位數如果增加，請直接寫入;Nonce 位數如果減少，請在前面補0到原本的位數，避免檔案大小減少。**

The first line contains two numbers $n$ and $q$ (separated by a space), representing the number of block files and the number of tampering commands.

The next $n$ lines contain block file names (`block_i_1.txt`, ..., `block_i_n.txt`). The file names are guaranteed to be in sequential order.

The following $q$ lines each contain three numbers $x, y, z$ (separated by spaces), instructing you to modify `<data y>` in `block_i_x.txt` to `z`.

**We guarantee that the original `<data y>` and the number `z` have the same number of digits, so you can directly overwrite the data without worrying about shifting the file's contents. (The Nonce does not share the same digit-length guarantee.)**

**If the number of digits in the Nonce increases, write it directly; if the number of digits decreases, prepend zeros to match the original number of digits to avoid reducing the file size.**
```
n q
block_i_1.txt
block_i_2.txt
.
.
block_i_n.txt
x1 y1 z1
x2 y2 z2
x3 y3 z3
.
.

```

### Output Format
輸出只有一個數字

請輸出 $q$ 個竄改指令中，有多少指令是執行不影響雜湊值的竄改操作

Output a single number.

Output the number of tampering commands out of the $q$ total that resulted in no change to the hash value without modifying the Nonce.
```
<number of command which doesn't modify hash without changing Nonce>
```
檔案中，請依照指令竄改資料，並適時更改 Nonce。只有輸出及更改後的檔案皆正確才會被判為通過測資

Additionally, ensure that both the output and the modified files are correct to pass the testcases.


### Constrain
$1 \leq n \leq 20$

$1 \leq k \lt 5000,\; for\ all\ blocks$

$1 \leq q \leq 1000$

$0 \leq previous\ hash,\ data,\ Nonce \lt 2^{30}$

$1 \leq x \lt n$

### Testcase Group
- **Subtask 0~3 (20 point)**
    - $1 \leq n \leq 10$
    - $1 \leq k \lt 10,\; for\ all\ blocks$
    - $1 \leq q \leq 10$
- **Subtask 4~5 (20 point)**
    - $1 \leq k \lt 25,\; for\ all\ blocks$
    - $1 \leq q \leq 25$
- **Subtask 6~7 (30 point)**
    - $1 \leq k \lt 500,\; for\ all\ blocks$
- **Subtask 8~9 (30 point)**
    - $no\ other\ constrain$

### Sample Input 1

### Sample Output 1

### Sample Input 2

### Sample Output 2
