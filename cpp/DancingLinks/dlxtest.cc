/*
 Let's suppose we want to solve this matrix:
 101
 111
 100
 ...where all rows are primary
 every row is introduced to the C++ class in a SPARSE way: only column positions with a 1 are introduced:
  r\c| 012  
 ----------
  0  | 100  -> only column 0
  1  | 101  -> columns 0 and 2
  2  | 111  -> columns 0, 1, 2
 results are given as sets of row indices in a vector of size the number of rows
 Constructor needs the number of rows, columns and the maximum number
 of 1s in the matrix (columns*rows allways work since this is an upper
 bound)
*/

using namespace std;
#include <iostream>
#include "dlx.cc"

int main() {
	dlx dlx_solver(3 /*rows*/,3 /*cols*/,6 /*no. of '1' elements*/);

	dlx_solver.insert_element(0);	// 100
	dlx_solver.end_row();
	dlx_solver.insert_element(0);	// 101
	dlx_solver.insert_element(2);
	dlx_solver.end_row();
	dlx_solver.insert_element(0);	// 111
	dlx_solver.insert_element(1);
	dlx_solver.insert_element(2);
	dlx_solver.end_row();

	int rows[3];
	int length;
	cout << "Numrows: "<< dlx_solver.get_num_rows() << endl;
	// one iteration for every solution
	while (dlx_solver.get_solution(rows,length)) {
	  cout << "A solution:\n";
	  for (int i=0;i<length;i++)
	    cout << "row number " << rows[i] << endl;
	}
	return 0;
}
