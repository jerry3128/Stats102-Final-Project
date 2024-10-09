#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
int main(){
	string s1 = "dflat -p /home/ubuntu/stats102-Final/env_dflat/dflat/applications/graph_problems/3col/dynamic.lp --print-decomposition --depth 0";
        for(int j=1;j<=10;j++){
		for(int i=1;i<=200;i++){
			string curf = "/home/ubuntu/stats102-Final/code/Result/data/data" + to_string(i) + "/data" + to_string(i) + ".gr";
			string curo = "/home/ubuntu/stats102-Final/code/Result/data/data" + to_string(i) + "/data" + to_string(i) + "_" + to_string(j) + ".td";
			string cmd = s1 + " < " + curf + " > " + curo;
			cout<<cmd<<"\n";
			system(cmd.c_str());
		}
		sleep(1);

	}
	return 0;
}
