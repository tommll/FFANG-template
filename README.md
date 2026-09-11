# Chào mừng đến với khoá học FSE17-FAANG

## Giới thiệu chung
1. Đây là nơi chứa live coding và bài tập, sau mỗi buổi học các bạn sẽ có bài tập về nhà để luyện tập
2. Để nộp bài tập về nhà, hãy tạo nhánh mới, làm bài tập trong thư mục homework ở mỗi buổi học, commit code changes và tạo `Pull Request`

## 🏆 BẢNG XẾP HẠNG nộp bài tập về nhà
- `FSE Bot` có thống kê số bài tập về nhà mà bạn nộp theo từng buổi và theo tổng khoá học, sau đó sẽ cập nhật bảng xếp hạng vào channel `#bang-xep-hang`.
- Điểm số được tính theo số lượng bài tập mà các bạn đã nộp. Trong trường hợp 2 thành viên có cùng điểm số, thì người nào nộp trước sẽ được xếp hạng trước.
- Để `FSE Bot` đếm bài tập hợp lệ, thì các bạn **phải làm bài tập trong thư mục `homework` của mỗi buổi học** và **không close Pull Request** nhé. Chi tiết cách nộp bài ở bên dưới.

<img width="1197" alt="image" src="https://raw.githubusercontent.com/FSEOrg/FSE-images/refs/heads/main/leaderboard1.png">

<img width="1212" alt="image" src="https://raw.githubusercontent.com/FSEOrg/FSE-images/refs/heads/main/leaderboard2.png">


## Hướng dẫn nộp bài - Có 2 cách
**LƯU Ý: Các bạn không merge branch của mình vào `main` branch và không push code trực tiếp lên `main` branch.**

### Cách 1: Dùng Github Desktop
- Bước 1: Tải Github Desktop tại đây: https://desktop.github.com/
- Bước 2: Clone repository `https://github.com/FSEOrg/FSE17-FAANG.git` về máy của bạn

  *Hướng dẫn: Chọn `File -> Clone repository`, chọn tab URL, paste link đó vào.*
  <img width="498" alt="image" src="https://raw.githubusercontent.com/FSEOrg/FSE-images/refs/heads/main/github1.png">


Sau mỗi buổi học, các bạn sẽ thấy thư mục mới cho bài tập ở master branch tương ứng với số bài học. Ví dụ: sau bài học số 3, ở master branch sẽ có folder hw03. Trong mỗi folder sẽ có 2 subfolders

      - `livecoding`: chứa các đoạn code demo trong buổi học
      - `homework`: chứa các bài tập về nhà cho buổi học, bạn sẽ cần làm bài và nộp bài trong thư mục này.
- Bước 3: Tạo branch mới, nên đặt tên theo cú pháp `hw[mã buổi học]-[tencuaban]`, ví dụ `hw02-maithanhhiep`

  *Hướng dẫn: Nhấn nút chỗ `Current Branch` (phần khoanh đỏ), nhấn nút `New branch`, nó sẽ hiển thị hộp thoại giống bên dưới, hãy đặt tên branch của bạn và nhấn nút `Create Branch`*
  <img width="959" alt="Screenshot 2024-10-01 at 08 58 23" src="https://raw.githubusercontent.com/FSEOrg/FSE-images/refs/heads/main/github2.png">



- Bước 4: Khi bạn làm bài tập, những đoạn code changes của bạn sẽ hiển thị ở đây. Chọn những file cần commit, đặt tên commit (ví dụ `HW02 - Mai Thành Hiệp`) và nhấn nút `Commit to {branch_name}` (màu xanh dương)
  <img width="964" alt="image" src="https://raw.githubusercontent.com/FSEOrg/FSE-images/refs/heads/main/github3.png">

- Bước 5: Push code đã commit lên remote, bằng cách nhấn nút `Publish branch`
  <img width="959" alt="Screenshot 2024-09-29 at 17 29 33" src="https://raw.githubusercontent.com/FSEOrg/FSE-images/refs/heads/main/github4.png">
  
- Bước 6: Mở trang web https://github.com/FSEOrg/FSE17-FAANG , bạn sẽ thấy có nút để tạo Pull Request, hãy tạo Pull Request để các giảng viên review nhé.

  **Lưu ý: Nên đặt tên Pull Request theo format `HW[MÃ BUỔI HỌC] - TÊN CỦA BẠN`, ví dụ `HW02 - Mai Thành Hiệp` để giảng viên dễ review code nhé.**

### Cách 2: Dùng Git Command
 1. Các bạn có thể tham khảo thêm về cách dùng Git/Github ở đây:  [https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

 2. Nếu đây là lần đầu bạn đến với repo này thì bạn cần clone project này trước
    ```
    git clone https://github.com/FSEOrg/FSE17-FAANG.git
    cd FSE17-FAANG
    ``` 
 3. Sau mỗi buổi học, các bạn sẽ thấy thư mục mới cho bài tập ở master branch tương ứng với số bài học. Ví dụ: sau bài học số 3, ở master branch sẽ có folder hw03. Trong mỗi folder sẽ có 2 subfolders
    - ```livecoding```: chứa các đoạn code demo trong buổi học
    - ```homework```: chứa các bài tập về nhà cho buổi học
 4. Các bạn hãy pull code mới nhất từ master branch về máy (bạn hãy chắc chắn mình đang ở ```main``` branch trước khi tiếp tục, có thể kiểm tra branch hiện tại bằng lệnh ```git branch```)
    ```
    cd FSE17-FAANG
    git checkout main
    git status  -> hãy kiểm tra bạn đang ở main branch
    git pull origin main
    ```
 5. Tại máy của bạn, tạo branch mới với tên nên thuộc format sau: hw[mã buổi học]-[tencuaban]. Tên branch của bạn cần có format này để review. Ví dụ: ```hw02-maithanhhiep``` nếu như bạn đang làm bài tập cho buổi số 2 và tên của bạn là *maithanhhiep* 
	 ```
	 git checkout -b hw02-maithanhhiep
	 ```
 6. Bạn hãy viết lời giải vào file tương ứng với mỗi bài tập trong slide buổi học và commit tất cả lới giải và push lên remote branch của bạn. Bạn có thể tạo nhiều commit, miễn là bạn push tất cả code của bạn lên repo trước deadline để được review code.
    
    Để xem lại những file đã thay đổi bạn gõ `git status`
    - Những file màu đỏ: Là những file đã thay đổi nhưng chưa được add vào git để chuẩn bị commit
    - Những file màu xanh: Là những file đã thay đổi và đã được add vào git để chuẩn bị commit

    <img width="806" alt="image" src="https://raw.githubusercontent.com/FSEOrg/FSE-images/refs/heads/main/git-cmd.png">
    
    Để quản lý những file cần add vào git để chuẩn bị commit
    - Muốn add file nào vào git để commit thì cú pháp `git add "ten file"`
    - Muốn loại bỏ file nào khỏi việc commit thì cú pháp `git restore --unstage "ten file"`
    - Muốn add tất cả các file vào git để commit thì cú pháp `git add .` (cái này sẽ add tất cả các file bao gồm các file rác nên cẩn thận)

    Kiểm tra lại những file mình cần commit đều được chuyển sang màu xanh hết chưa
    ```
    git status
    ```

    Commit code và push lên remote
    ```
    git commit -m 'HW02 - Ten Cua Ban'
    git push origin hw02-maithanhhiep
    ```
 7. Mở trang web https://github.com/FSEOrg/FSE17-FAANG , bạn sẽ thấy có nút để tạo Pull Request, hãy tạo Pull Request để các giảng viên review nhé.

    **Lưu ý: Nên đặt tên Pull Request theo format `HW[MÃ BUỔI HỌC] - TÊN CỦA BẠN`, ví dụ `HW02 - Mai Thành Hiệp` để giảng viên dễ review code nhé.**
