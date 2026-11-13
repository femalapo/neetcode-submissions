class MinStack {
public:
    int size;
    int maxSize;
    int* mainArr;
    int* minArr;

    MinStack() {
        maxSize = 2;
        size = 0;
        mainArr = new int[maxSize];
        minArr = new int[maxSize];
    }
    
    void push(int val) {
        if(size == 0){
            minArr[size] = val;
        }
        else
        {
            minArr[size] = min(val, minArr[size-1]);
        }

        mainArr[size] = val;
        size++;

        if(size >= maxSize / 2){
            maxSize *= 2;
            resizeArr(maxSize);
        }
    }
    
    void pop() {
        size--;

        if(size > 2 && size <= maxSize / 4){
            maxSize /= 2;
            resizeArr(maxSize);
        }
    }
    
    int top() {
        return mainArr[size - 1];
    }
    
    int getMin() {
        return minArr[size - 1];
    }

    void resizeArr(int s){
        int* newMainArr = new int[s];
        copy_n(mainArr, size, newMainArr);
        delete[] mainArr;
        mainArr = newMainArr;

        int* newMinArr = new int[s];
        copy_n(minArr, size, newMinArr);
        delete[] minArr;
        minArr = newMinArr;
    }
};
