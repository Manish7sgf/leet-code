// Last updated: 7/14/2026, 2:18:16 PM
class Solution {
    public String multiply(String num1, String num2) {
        int a=num1.length();
        int b=num2.length();
        if(num1.equals("0")||num2.equals("0")) return "0";
        int r[]=new int[a+b];
        for(int i=a-1;i>=0;i--)
        {
            for(int j=b-1;j>=0;j--)
            {
                int mul=(num1.charAt(i)-'0')*(num2.charAt(j)-'0');
                int sum=mul+r[i+j+1];
                r[i+j+1]=sum%10;
                r[i+j]+=sum/10;
            }
        }
        StringBuilder sb=new StringBuilder();
        for(int num:r)
        {
            if (!sb.isEmpty() || num!=0) sb.append(num);
        }
        return sb.toString();
    }
}