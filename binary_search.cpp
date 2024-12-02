#include<bits/stdc++.h>
using namespace std;

int binarySearch(int arr[], int target, int n)
{
    int low = 0, high = n;
    while(low <= high)
    {
        int mid = (low + high) / 2;
        if(arr[mid] == target)
            return mid;
        else if (arr[mid] > target)
            high = mid - 1;
        else if (arr[mid] < target)
            low = mid + 1;
    }
    return -1;
}

int main()
{
    int n, target;
    cin >> n;

    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];
    
    cin >> target;

    sort(arr, arr + n);
    printf("Sorted array: \n");
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
    
    int idx = binarySearch(arr, target, n);
    
    if(idx >= 0)
        printf("%d is at index %d\n", target, idx);
    else
        printf("Not Found!\n");
    return 0;
}
