# Linked List Tutorial

## Introduction

A linked list is a linear structure connected by pointers. Each node consists of two parts, one is the data field and the other is the pointer field (which stores the pointer to the next node), and the pointer field of the last node points to null (null pointer).

We only discuss doubly-linked list here since it is usually much more useful than singly-linked lish.

![Linked list](linked_list.png)

In the linked list, the first node is called the *head* and the last node is called the *tail*. Each element in the linked list is called a *node*. And each node has two pointers, which are *previous* and *next*. Previous points to the last node and next points to the next node.

## How Linked List Stores Elements in Memory

Arrays are distributed continuously in memory, but linked lists are not distributed continuously in memory.

A linked list is linked to each node in the memory through the pointer of the pointer field.

Therefore, the nodes in the linked list are not continuously distributed in the memory, but scattered at an address in the memory. The allocation mechanism depends on the memory management of the operating system.

![store methoed](store.png)

## Insert and Delete
Linked lish in python is more complicated than stack. Insert and delete an element takes a few steps but they are efficient that both of their efficiency are O(1). But if you want to insert or remove an element in the middle, you have to find where that element is. This process takes O(n) to compete.
For example, if you want to remove the fifth element, you have to find where the next pointer of the forth element and the previous pointer of the sixth element are.


