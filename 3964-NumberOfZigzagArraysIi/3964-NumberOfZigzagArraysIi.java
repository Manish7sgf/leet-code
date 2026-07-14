// Last updated: 7/14/2026, 2:16:55 PM
class Solution {
    static final long MOD=1000000007L;
    public int zigZagArrays(int n, int l, int r) {
        int m=r-l+1;
        int size=2*m;
        long trans[][]=new long[size][size];
        for(int x=0;x<m;x++)
        {
            for(int y=0;y<m;y++)
            {
                if(x<y)
                {
                    trans[y][m+x]=1;
                }
                if(x>y)
                {
                    trans[m+y][x]=1;
                }
            }
        }
        long base[]= new long[size];
        for(int x=0;x<m;x++)
        {
            for(int y=0;y<m;y++)
            {
                if(x<y) base[y]++;
                if(x>y) base[m+y]++;
            }
        }
        long power[][]=matrixPower(trans,n-2);
        long result[]=multiply(base,power);
        long ans=0;
        for(long v:result)
        {
            ans=(ans+v)%MOD;
        }
        return (int) ans;
    }
    private long[] multiply(long[] vec,long[][] mat)
    {
        int n=vec.length;
        long res[]=new long[n];
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<n;k++)
            {
                res[j]=(res[j]+vec[k]*mat[k][j])%MOD;
            }
        }
        return res;
    }
    private long [][] matrixPower(long[][]mat,int exp)
    {
        int n=mat.length;
        long res[][]=new long[n][n];
        for(int i=0;i<n;i++)
        {
            res[i][i]=1;
        }
        while(exp>0)
        {
            if((exp&1)==1)
            {
                res=multiply(res,mat);
            }
            mat=multiply(mat,mat);
            exp>>=1;
        }
        return res;
    }
    private long[][] multiply(long[][]a,long[][]b)
    {
        int n=a.length;
        long res[][]=new long[n][n];
        for(int i=0;i<n;i++)
        {
            for(int k=0;k<n;k++)
            {
                if(a[i][k]==0) continue;
                for(int j=0;j<n;j++)
                {
                    res[i][j]=(res[i][j]+a[i][k]*b[k][j])%MOD;
                }
            }
        }
        return res;
    }
}