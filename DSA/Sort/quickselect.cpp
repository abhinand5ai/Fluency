#include <iostream>
#include <vector>
#include <random>
using namespace std;

typedef vector<int> vi;

void swp(vi &arr, int i, int j)
{
    int tmp = arr[j];
    arr[j] = arr[i];
    arr[i] = tmp;
}

int partition(vi &arr, int start, int end)
{
    int pivot = start + (rand() % (end - start + 1));
    int pv = arr[pivot];
    int le = start, gt = end;

    while (le < gt)
    {
        if (arr[gt] > pv)
        {
            gt -= 1;
        }
        else
        {
            le += 1;
            swp(arr, le, gt);
        }
    }
    swp(arr, le, start);
    return le;
}

void quickSelect(vi &arr, int k)
{

    int start = 0, end = arr.size() - 1;
    int p = 0;
    while (true)
    {
        p = partition(arr, start, end);
        if (k < p)
            end = p - 1;

        else if (p < k)
            start = p + 1;
        else
            return;
    }
}

int findKthLargest(vi arr, int k)
{

    quickSelect(arr, arr.size() - k);
    return arr[arr.size() - k];
}

int main()
{
    vi arr = {3, 3, 2, 1, 5, 6, 4};
    int kth = findKthLargest(arr, 4);
    printf("Kth largest element %d\n", kth);

    return 0;
}