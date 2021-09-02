#include<iostream>

using namespace std;

bool isSafe(int **arr, int x, int y, int N){
	// coulumn check (y)
	for(int row=x-1; row>=0; --row){
		if(arr[row][y] == 1)
			return false;
	}

	// // diagnol check
	int temp_y = y;
	for(int row=x; row>0; row--){
		if(arr[row][temp_y] == 1)
			return false;
		temp_y++;
	}

	temp_y = y;
	for(int row=x; row>0; row--){
		if(arr[row][temp_y] == 1)
			return false;
		temp_y--;
	}
	return true;

	// for(int row=0; row<x; row++){
	// 	if(arr[row][y] == 1){
	// 		return false;
	// 	}
	// }

	// int row=x;
	// int col=y;
	// while(row>=0 && col>=0){
	// 	if(arr[row][col]==1)
	// 		return false;
	// 	row--;
	// 	col--;
	// }
	// row=x;
	// col=y;
	// while(row>=0 && col<N){
	// 	if(arr[row][col]==1)
	// 		return false;
	// 	row--;
	// 	col++;
	// }
	// return true;
}

bool nQueen(int **board, int x, int N){
	if(x>=N)
		return true;

	for(int col = 0; col<N; col++){

		if(isSafe(board, x, col, N)){
			board[x][col] = 1;
			if(nQueen(board, x+1, N))


			board[x][col] = 0; //backtracking
		}
	}
	return false;
}

int main(){
	int N;
	cin >> N;
	int **arr = new int*[N];

	for(int i=0; i<N; i++){
		arr[i] = new int[N];
		for(int j=0;j<N;j++){
			arr[i][j] = 0;
		}
	}

	if(nQueen(arr, 0, N)){
		for(int i=0; i<N; i++){
			for(int j=0;j<N;j++){
				cout << arr[i][j] << " ";
			}cout<< endl;
	}

	}

	// int board[N][N];
	// for(int i = 0; i<N; i++){
	// 	for(int j = 0; j<N; j++){
	// 		board[i][j] = 0;
	// 	}
	// }

	// for(int i = 0; i<N; i++){
	// 	cout << endl;
	// 	for(int j = 0; j<N; j++){
	// 		cout <<board[i][j]<< " ";
	// 	}
	// }
}