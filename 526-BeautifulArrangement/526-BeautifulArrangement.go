// Last updated: 8/31/2026, 1:58:46 PM
func countArrangement(n int) int {
    used := make([]bool, n+1)

    var backtrack func(int) int
    backtrack = func(pos int) int {
        if pos > n {
            return 1
        }

        count := 0
        for num := 1; num <= n; num++ {
            if !used[num] && (num%pos == 0 || pos%num == 0) {
                used[num] = true
                count += backtrack(pos + 1)
                used[num] = false
            }
        }
        return count
    }

    return backtrack(1)
}