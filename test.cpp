#include<bits/stdc++.h>
using namespace std;

class First{
	public:
	void func();
};
void First::func(){
	cout<<"This is member function defined outside the classi";
}

int main(){
	//Creating object of class
	First obj;

	//calling the member of class
	obj.func();
}
