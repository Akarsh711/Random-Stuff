#include<iostream>
using namespace std;

//count will help to track which object is constructing and Destructing
int count;
class A{
public:
	A(){
		count++;
		cout<<"Constructing Objects:"<<count<<endl;
	}

	~A(){
		cout<<"Deconstructing Objects:"<<count<<endl;
		count--;
	}

};

class B:A{};
int main(){

	A obj;
	{
		A *ptr = new A;
		//Distructor in Scope
		//A obj1;
		//A obj2;
		delete ptr;

	}


}
