#include "solution.h"

int main()
{
    AList<int> list1;
    list1.clear();
    for(int i=0;i<15;i++)
    {
        list1.append(i);
    }
    list1.showList();
    list1.moveToPos(5);
    int element=list1.remove();
    cout<<"the element is "<<element<<endl;
    list1.showList();
    list1.insert(100);
    int Pos=list1.currPos();
    cout<<"the 100 is inserted in "<<"pos:"<<Pos<<endl;
    list1.showList();
    return 0;
}