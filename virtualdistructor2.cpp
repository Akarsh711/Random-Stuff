#include<iostream>
using namespace std;

//Virtual Distructor

class A{
	int a;
	void func1(){
		cout"func1"<<endl;
	}		

};

class B: public A{
	int b;
	void func2(){
		cout<<"func2"<<endl;

	}

};


int fun();
int fun(){
	//In case of Inheritance you can make pointer of parent class and create object of child class
	//But this pointer can only invoke those memeber for child class which are in parent class(Early Binding) 
	//
	A *p = new B;
	p->func2();
}

int main(){
	fun();
}
