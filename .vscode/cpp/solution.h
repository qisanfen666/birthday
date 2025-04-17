#pragma once
#include <iostream>
#include <string>
using namespace std;
//#ifndef SOLUTION_H
//#define SOLUTION_H
template <typename T> class List
{
private:
	void operator =(const List&) {}
	List(const List&) {}
public:
	List() {}
	virtual ~List() {}

	virtual void clear() = 0;
	virtual void insert(const T& item) = 0;
	virtual void append(const T& item) = 0;
	virtual T remove() = 0;
	virtual void moveToStart() = 0;
	virtual void moveToEnd() = 0;
	virtual void prev() = 0;
	virtual void next() = 0;
	virtual int length() const = 0;
	virtual int currPos() const = 0;
	virtual void moveToPos(int pos) = 0;
	virtual const T& getValue() const = 0;
};

template <typename T>
class AList : public List<T>
{
private:
	int capacity;
	int size;
	int curr;
	T* listArray;
public:
	AList()
	{
		capacity = 10;
		size = curr = 0;
		listArray = new T[capacity];
	}
	~AList()
	{
		delete[] listArray;
	}

	void resize()
	{
		T* newListArray=new T[capacity*2];
		for(int i=0;i<size;i++) newListArray[i]=listArray[i];
		delete[] listArray;
		listArray=newListArray;
		capacity*=2;
	}


	void clear()//delete,recreate the array
	{
		delete[] listArray;
		capacity=10;
		size = curr = 0;
		listArray = new T[capacity];
	}

	void insert(const T& it)
	{
		if(size>=capacity) resize();        
		for (int i = size; i > curr; i--) listArray[i] = listArray[i - 1];
		listArray[curr] = it;
		size++;
        
		
	}

	void append(const T& it)
	{
		if(size>=capacity) resize();   
        listArray[size] = it;
		size++;		
	}

	T remove()
	{
		T it = listArray[curr];
		for (int i = curr; i < size - 1; i++) listArray[i] = listArray[i + 1];
		size--;
		return it;
	}

	void moveToStart() { curr = 0; }
	void moveToEnd() { curr = size; };
	void prev() { if (curr > 0) curr--; }
	void next() { if (curr < size) curr++; }
	void moveToPos(int pos)
	{
		curr = pos;
	}

	int length() const { return size; }
	int currPos() const { return curr; }
	const T& getValue() const
	{
		return listArray[curr];
	}

	void showList()
	{
		int Pos=currPos();
		for(curr=0;currPos()!=size;next()) cout<<getValue()<<endl;
        moveToPos(Pos);
	}
};

//#endif