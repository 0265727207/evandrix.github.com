#include <cstdio>
#include <cstdlib>
#include <stdint.h>
using namespace std;

typedef struct _ITEM {
    int id;
    struct _ITEM *m_NextPrev;
} Item;

template <class T>
class DoubleLinkedXOR
{
public:
    DoubleLinkedXOR() {
        m_head = m_tail = 0;
    }
    ~DoubleLinkedXOR() {}

    void AddToTail(T entry) {
        if(!m_head) { //no items
            entry->m_NextPrev = 0;
            m_head = entry;
        } else if(!m_tail) { //just head is set, one item in list
            m_tail = entry;
            m_tail->m_NextPrev = m_head;
            m_head->m_NextPrev = m_tail;
        } else { //two items or more, insert
            entry->m_NextPrev = m_tail;
            m_tail->m_NextPrev = (T)((intptr_t)(m_tail->m_NextPrev) ^ (intptr_t)entry);
            m_tail = entry;
        }
    }
    T RemoveFromHead() {
        T item = m_head;

        if(!m_head) {
            return 0;
        } else if(!m_tail) { //just one item
            m_head = 0;
            return item;
        } else if(m_head->m_NextPrev == m_tail
                  && m_tail->m_NextPrev == m_head) { // only two items
            m_head = m_tail;
            m_tail = 0;
            m_head->m_NextPrev = 0;
            return item;
        } else {
            m_head = m_head->m_NextPrev;
            m_head->m_NextPrev = (T)((intptr_t)(m_head->m_NextPrev) ^ (intptr_t) item);
            return item;
        }
    }
private:
    T m_tail;
    T m_head;
};

int main(int argc, char *argv[])
{
    DoubleLinkedXOR <Item*> *list = new DoubleLinkedXOR<Item*> ();
    int x, count = 10;

    for(x = 0;  x < count; x++) { //add all items to list
        Item *newItem = (Item*)malloc(sizeof(Item));
        newItem->id = x;
        list->AddToTail(newItem);
        printf("Added item: %d\n", newItem->id);
    }

    for(x = 0; x < count; x++) {
        Item *retrievedItem = list->RemoveFromHead();
        printf("Retrieved item: %d\n", retrievedItem->id);
        free(retrievedItem);
    }

    delete list;
    return 0;
}
