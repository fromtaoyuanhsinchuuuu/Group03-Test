# 布拉格錢數位帳本-有漏洞？！那我親自來
The English version was translated by ChatGPT. We have done our best to maintain the accuracy of the problem description to ensure that you will not misunderstand the requirements.

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
![Block_Chain](https://github.com/fromtaoyuanhsinchuuuu/Group03-Test/blob/main/image/Block_Chain.jpeg?raw=true)

一條區塊鏈是由數個區塊(block)組成，每個區塊內容須包含三個部份：前一個區塊的雜湊值(previous hash)、數筆資料(data)、以及特殊數字 Nonce。

- previous hash 是由上一個區塊內容計算來的，是形成鏈狀結構的關鍵。
- data 在我們的題目只會以數字的型態存在，以方便計算區塊的雜湊值(hash)。
- 特殊數字 Nonce 並不像前兩者一樣具有紀錄功能。Nonce 是單純用來改變區塊的雜湊值(hash)的數字，在計算區塊雜湊值的時候會被使用。

一個區塊的雜湊值是根據區塊內容及使用的雜湊函數決定的，在此我們將用文字檔案模擬區塊（一個文字檔案代表一個區塊）、並使用自定義的雜湊函數（詳見下方雜湊函數），進行布拉格錢數位帳本的竄改。

A blockchain consists of several blocks, each containing three parts: the previous block's hash (previous hash), several pieces of data (data), and a special number called Nonce.

- The `previous hash` is computed by the content of previous block. It is the key to forming the chain-like structure. 
- The `data` will only exist in numeric form in this problem for ease of computation of the block's hash value.
- The special number `Nonce` does not have a record-keeping function like the first two components. Nonce is purely a number used to change the block's hash value (hash).

A block's hash value is determined by its contents and the hash function used. Here, we simulate blocks with text files (one text file represents one block) and use a custom hash function (described below) to perform the tampering operation on the PragueCoin digital ledger.


### 題目敘述 Problem Description
給定兩數字 $n$ 和 $q$，以及 $n$ 個區塊檔案名稱 (`block_i_1.txt`, `block_i_2.txt`, ..., `block_i_n.txt`)和 $q$ 個竄改指令（`x1 y1 z1`, `x2 y2 z2`, ..., `xq yq zq`）。請依照輸入的指令將 `block_i_x.txt` 的 `<data y>` 竄改 成數字 `z` ，並**適時**更改區塊 Nonce，使得區塊雜湊值維持不變。

沒錯，「**適時**更改 Nonce」代表某些情況下竄改操作並不會影響區塊雜湊值，也就不會需要調整 Nonce 來確保雜湊值不變。請紀錄 $q$ 個竄改指令中，有多少指令是執行**不影響雜湊值**的竄改操作，並將紀錄結果輸出。

另外，因為最後一個區塊沒有對應的 previous hash，所以我們的竄改指令不會要求竄改最後一個區塊的資料。

Given two numbers, $n$ and $q$, as well as $n$ block file names (`block_i_1.txt`, `block_i_2.txt`, ..., `block_i_n.txt`) and $q$ tampering commands (`x1 y1 z1`, `x2 y2 z2`, ..., `xq yq zq`). According to the given commands, please modify the `<data y>` in `block_i_x.txt` to the value `z`. Additionally, **appropriately** adjust the Nonce of the block to ensure that the block's hash value remains unchanged.


Yes, "**appropriately** adjust the Nonce" means that in some cases, tampering operations may not affect the block's hash value, so no Nonce adjustment is needed to ensure the hash value remains the same. Record how many of the $q$ tampering commands resulted in hash values that were unaffected and output the record.

Additionally, since the last block does not have a corresponding `previous hash`, tampering commands will not require modifying the data of the last block.


### 檔案格式 File Format
與作業有所不同，並且對於如何讀寫相當重要，請詳細閱讀

檔名固定為 `block_i_j.txt`，其中 $i$ 為測資的編號， $j$ 為區塊的編號。檔案內容格式如下

Differs from the assignment and important to read/write file correctly, please read carefully.

File names are fixed as `block_i_j.txt`, where $i$ represents the test case index and $j$ represents the block number. The file content is formatted as follows:
```
P: <pre-hash>
<data 1>
<data 2>
.
.
<data k>
N: <nonce>
```
- 檔案中所有數字皆以十進位表示，請注意冒號後面的空格
- 第一行 `P: ` 後面的數字是 previous hash，為上一個區塊的雜湊值
    - 第一個區塊的 P 必為 0
    - **所有區塊的 previous hash 皆不可更動**
- 最後一行 `N: ` 後面的數字是 Nonce，用以計算或改變這個區塊的雜湊值 (詳見下方雜湊函數)
    - 最後一個區塊的 Nonce 必為 0
    - **無論 Nonce 是幾位數，前面將補0直到 Nonce 有十位**
    - **更改 Nonce 時，也請在數字前補0，直到 Nonce 有十位**
- 剩下的部份是區塊中的 data，會按照順序排好（如上方範例中 $1\ to\ k$）
    - 我們保證一個區塊至少會有一個 data
    - **與作業不同，這次 data 開頭沒有編號**
    - **這次我們保證同一個區塊檔案中的所有 data 都有相同的位數**
    - **竄後的數字也與原本 data 有相同位數**
    - **previous hash 與 nonce 的位數可能與 data 位數不同**
    - 這些改動方便同學計算 offset，並進行 random access
- All numbers in the file are represented in decimal format. And please pay attention to the space after the colon.
- The first line starts with `P: ` followed by a number, which is the `previous hash`, representing the hash value of the previous block.
    - The `P` in the first block must be `0`.
    - **The `previous hash` of all blocks cannot be modified.**
- The last line starts with `N: ` followed by a number, which is the `Nonce`, used to compute or adjust the hash value of the block (see the hash function below for details).
    - The `Nonce` of the last block must be `0`.
    - **Regardless of the number of digits in the `Nonce`, leading zeros will be added to ensure the `Nonce` has exactly 10 digits.**
    - **When modifying the `Nonce`, also add leading zeros so that the `Nonce` has exactly 10 digits.**
- The rest of the block contains `data`, ordered sequentially (e.g., from $1$ to $k$ as shown in the example above).
    - We guarantee that each block will have at least one `data` entry.
    - **The `data` entries do not have a prefix numbering. This is different from HW**
    - **We guarantee that all `data` entries in the same block file have the same number of digits.**
    - **Modified `data` will also match the original number of digits.**
    - **The number of digits in `previous hash` and `Nonce` may differ from that of the `data`.**
    - These adjustments are made to help your calculate offsets and perform random access.


### 雜湊函數 (Hash function)
**Nonce 運算部份與作業不同，請多加注意**

雜湊函數定義如下，將區塊的所有 data 以及 Nonce 進行運算即可得到區塊的雜湊值（不會使用到 previous hash）
- 初始 $H_0=0$
- 依照下列式子反覆運算
    - ![Hash Function](https://github.com/fromtaoyuanhsinchuuuu/Group03-Test/blob/main/image/Hash_Function.jpg?raw=true)
    - 假設區塊中有 $k$ 個data，則 $i\ from\ 1\ to\ k$
    - $d_i$ 就是 \<data $i$ \>
- 最後用 $H=Nonce \oplus H_k$
- 共 k+1 次運算後， $H$ 就是這個區塊的雜湊值

註： $\oplus$ 代表 XOR、 $\ll$ 代表邏輯左移、 $mod$ 代表取模


**Computation with Nonce is different from HW**

The hashing function is defined as follows. Compute the block's hash value by operating on all its `data` entries and the `Nonce`:
- Initial $H_0=0$ .
- Repeatedly compute using the formula:
    - ![Hash Function](https://github.com/fromtaoyuanhsinchuuuu/Group03-Test/blob/main/image/Hash_Function.jpg?raw=true)
    - Assume the block contains $k$ data entries; iterate $i\ from\ 1\ to\ k$ .
    - $d_i$ represents `<data i>`.
- $H= Nonce \oplus H_k$
- After k+1 computations, $H$ is the hash value of the block.

Note: $\oplus$ denotes XOR, $\ll$ denotes logical left shift, and $mod$ denotes modulus.


### Input Format
第一行只有兩個數字 $n$ 和 $q$（中間以空格隔開），代表有 $n$ 個區塊檔案及 $q$ 個需要竄改指令

接著 $n$ 行是檔案名稱，block_i_j.txt ( j $from\ 1\ to\ n$ )，我們保證檔名會照順序排好

最後 $q$ 行，每行皆有三個數字 $x, y, z$（中間以空格隔開），請將 block_i_x.txt 中的 \<data y> 改成 z

The first line contains two numbers $n$ and $q$ (separated by a space), representing the number of block files and the number of tampering commands.

The next $n$ lines contain block file names (`block_i_1.txt`, ..., `block_i_n.txt`). The file names are guaranteed to be in sequential order.

The following $q$ lines each contain three numbers $x, y, z$ (separated by spaces), instructing you to modify `<data y>` in `block_i_x.txt` to `z`.
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
xq yq zq
```

### Output Format
輸出只有一個數字，請輸出 $q$ 個竄改指令中，有多少指令是執行不影響雜湊值的竄改操作

Output just a single number, the number of tampering commands out of the $q$ total that resulted in no change to the hash value without modifying the Nonce.
```
<number of command which doesn't modify hash without changing Nonce>
```
檔案中，請依照指令竄改資料，並適時更改 Nonce。只有輸出及更改後的檔案皆正確才會被判為通過測資

Additionally, ensure that both the output and the modified files are correct to pass the testcases.

### Constrain
$1 \leq n \leq 20$

$1 \leq k \lt 5000,\ for\ all\ blocks$

$1 \leq q \leq 1000$

$0 \leq previous\ hash,\ data,\ Nonce \lt 2^{30}$

$1 \leq x \lt n$

### Testcase Group
- **Subtask 0~1 (0 point)**
    - Sample Testcases
- **Subtask 2~3 (20 point)**
    - $1 \leq n \leq 10$
    - $1 \leq k \lt 10,\ for\ all\ blocks$
    - $1 \leq q \leq 10$
- **Subtask 4~5 (20 point)**
    - $1 \leq k \lt 25,\ for\ all\ blocks$
    - $1 \leq q \leq 25$
- **Subtask 6~7 (30 point)**
    - $1 \leq k \lt 500,\ for\ all\ blocks$
- **Subtask 8~9 (30 point)**
    - $no\ other\ constrain$

### Sample Input 1
stdin
```
2 1
block_0_1.txt
block_0_2.txt
1 1 1
```

block_0_1.txt (before)
```
P: 0
3
8
N: 0097384043
```

block_0_2.txt (before)
```
P: 97384032
4
3
N: 0000000000
```

### Sample Output 1
stdout
```
0
```

block_0_1.txt (after)
```
P: 0
1
8
N: 0097384041
```

block_0_2.txt (after)
```
P: 97384032
4
3
N: 0000000000
```
`x y z` 為 `1 1 1` ，將 `block_0_1.txt` 中第一個 data (原先為 `3` ) 改為 `1`。並更改其最後一行的 Nonce 使得雜湊值不變（記得變補0使 Nonce 有十位）

沒有 不需更改 Nonce 的指令，輸出 `0`

`x y z` is `1 1 1`, modify the first `data` in `block_0_1.txt` (originally `3`) to `1`. Update the last line's `Nonce` to ensure the hash value remains unchanged (remember to pad with leading zeros to make the `Nonce` 10 digits).

There are no commands that "No Require Changing the `Nonce` ", output `0`.


### Sample Input 2
stdin
```
2 1
block_1_1.txt
block_1_2.txt
1 1 4
```

block_1_1.txt (before)
```
P: 0
4
N: 0023124537
```

block_1_2.txt (before)
```
P: 23124541
2
N: 0000000000
```

### Sample Output 2
stdout
```
1
```

block_1_1.txt (after)
```
P: 0
4
N: 0023124537
```

block_1_2.txt (after)
```
P: 23124541
2
N: 0000000000
```
`x y z` 為 `1 1 4` ，將 `block_1_1.txt` 中第一個 data (原先為 `4` ) 改為 `4`。數字不變，所以不需要更改 Nonce 

有一個 不需更改 Nonce 的指令，輸出 `1`

$Hint:$ 不需更改 Nonce 的指令**並不是只有**「竄改資料與原本資料相同」這種狀況

`x y z` is `1 1 4`, modify the first `data` in `block_1_1.txt` (originally `4`) to `4`. Since the number remains unchanged, updating the `Nonce` is not required.

There is one command where updating the `Nonce` is not required, output `1`.

$Hint:$ Commands without updating the `Nonce` are **not limited to** cases where the modified data is the same as the original data.
