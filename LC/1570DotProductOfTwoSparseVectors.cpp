#include <iostream>
#include <vector>

#define PB push_back

using namespace std;

typedef vector<int> vi;

void printVector(vi& nums);

class SparseVector {
private:
	vi nums;
	int size;
	void append(vi& acc){
		this->nums.PB(acc.size());
		for (auto a : acc){
			this->nums.PB(a);
		}
	}
public:
    SparseVector(vi &original) {
		vi acc;
		int zeros = 0;
		this->size = original.size();
		for (auto num : original){
			if (num == 0) {
				if (acc.size() != 0){
					append(acc);
				}
				acc.clear();
				zeros += 1;
			} else {
				if(zeros != 0){
					this->nums.PB(zeros);
					this->nums.PB(0);
				}
				acc.PB(num);
				zeros = 0;
			}
		}

		if (acc.size() != 0){
			append(acc);
		}

		if(zeros != 0){
			this->nums.PB(zeros);
			this->nums.PB(0);
		}

    }

	bool nextNonZero(int* i, int* j, int* l){
		printf("%d %d %d\n", *i, *j, *l);
		if (*i == size - 1){
			return false;
		}
		if (*l == 0 ){
			*j += 1;
			*l = this->nums[*j];
			return nextNonZero(i, j, l);
		} else if ( nums[*j + 1] == 0) {
			*i += *l;
			*j += 1;
			*l = 0;
			return nextNonZero(i, j, l);
		} else{
			*i += 1;
			*j += 1;
			*l -= 1;
			return true;
		}
	}
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector& vec) {
		int i1, j1, l1;
		int i2, j2, l2;
		i1 = i2 = j1 = j2 = -1;
		l1 = l2 = 0;
		int dotP = 0;
		nextNonZero(&i1, &j1, &l1);
		vec.nextNonZero(&i2, &j2, &l2);
		while(true){
			if (i1 < i2) {
				if(!nextNonZero(&i1, &j1, &l1)){
					return dotP;
				}
			}
			else if (i2 < i1) {
				if(!vec.nextNonZero(&i2, &j2, &l2)){
					return dotP;
				}
			}
			else {
				dotP += nums[j1] * vec.nums[j2];
				if(!vec.nextNonZero(&i2, &j2, &l2)){
					return dotP;
				}
				if(!nextNonZero(&i1, &j1, &l1)){
					return dotP;
				}

			}
		}
		return dotP;
    }

	void print(){
		printVector(this->nums);
	}
};

void printVector(vi& nums){
	for(auto a: nums){
		cout<<a<<",";
	}
	cout<<endl;
}


int main(){
	vi v1{0,0,0,1,2,3, 0, 0, 0, 5, 6, 7, 0, 0, 0};
	SparseVector sp1(v1);
	printVector(v1);
	sp1.print();
	int dotProduct = sp1.dotProduct(sp1);

	cout << dotProduct <<endl;

	return 0;

}
