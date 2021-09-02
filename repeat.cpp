#include<iostream>
using namespace std;
class pubg{
	int x=0;
public:
	void gun(){
		cout<<"enter a number:";
		cin>>x;
	}
	void nade(){
     cout<<"ENTER NO> IS:"<<x<<endl;

	}
	pubg operator +(pubg p){
	 pubg a;
	 a.x=x+p.x;
      return a;
	}
};

int main(){
pubg m1,m2,m3;
m1.gun();
m2.gun();
m3=m1+m2;
m3.nade();

}