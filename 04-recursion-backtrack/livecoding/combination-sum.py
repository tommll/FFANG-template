class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Ý tưởng:
        # Sử dụng backtrack để sinh ra tất các tập con có lặp của candidates sao cho 
        # tổng của chúng có thể = target
        # Thay vì sinh trực tiếp ra các tập con đó (ví dụ: [2, 2, 3]), ta sẽ sinh ra 
        # current_solution với số lần xuất hiện tương ứng của từng phần tử (ví dụ cho [2, 2, 3]
        # thì sinh [2, 1, 0, 0] trước với 2 là số lần xuất hiện của 2, 1 là số lần xuất hiện của 3, 0 và 0
        # là số lần xuất hiện của 6 và 7)
        
        # [2, 1, 0, 0]


        # [2, 2, 3]

        # TC: O(N * (target//min(candidates) + 1)^N)
        # Số tập con tối đa có thể có = (target//min(candidates) + 1)^N
        # Với mỗi tập con, convert_current_solution_to_candidate là O(N)
        # SC: O(N) (current_solution) + O(N * (target//min(candidates) + 1)) (res) + O(N) (recursion) 
        # = O(N * target//min(candidates))

        current_solution = []
        ans = []
        current_sum = 0

        def convert_current_solution_to_candidate() -> List[int]:
            """
            Convert current_solution to an actual unique combination
            e.g. from [2, 1, 0, 0] to [2, 2, 3]
            """
            res = []
            for i, freq in enumerate(current_solution):
                for j in range(freq):
                    res.append(candidates[i])
            return res

        def choose(i: int) -> None:
            """
            Choose the i-th element for current_solution
            """
            nonlocal current_sum
            if i == len(candidates):
                if current_sum == target:
                    candidate = convert_current_solution_to_candidate()
                    ans.append(candidate)
                return
            
            need = target - current_sum
            for j in range(need//candidates[i] + 1):
                current_solution.append(j)
                current_sum += j * candidates[i]
                choose(i + 1)
                current_sum -= j * candidates[i]
                current_solution.pop()
        
        choose(0)

        return ans



        # N phan tu, moi phan tu co the chon hoac khong chon --> 2^N
        # --> N bits
