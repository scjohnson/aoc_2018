#include<stdio.h> 
#include<stdlib.h> 
#include <cstring>
#include <iostream>
  
struct Node  
{ 
  int data; 
  struct Node *next; 
  struct Node *prev;
}; 

void insert_after(Node* node, Node* node_after){
    node->next->prev = node_after;
    node_after->next = node->next;
    node->next = node_after;
    node_after->prev = node;
}
  
void remove_node(Node* node){
    node->prev->next = node->next;
    node->next->prev = node->prev;
    free(node);
}

int main(int argc, char const *argv[])
{
    struct Node *head = (struct Node *)malloc(sizeof(struct Node));
    head->data = 0;
    head->next = head;
    head->prev = head;

    int num_players;
    int last_marble;
    sscanf(argv[1], "%d", &num_players);
    sscanf(argv[2], "%d", &last_marble);

    long int scores[num_players];
    for (int i = 0; i < num_players; ++i){
        scores[i] = 0;
    }

    Node* current_node = head;
    int player = 0;
    for (int i = 1; i <= last_marble; ++i){
        if (i % 23 == 0)
        {
            scores[player] += i;
            for (int j = 0; j < 8; ++j)
            {
                current_node = current_node->prev;
            }
            scores[player] += current_node->data;
            current_node = current_node->prev;
            remove_node(current_node->next);
            if (scores[player] < 0){
            std::cout << scores[player] << std::endl;
            }
        }
        else
        {
            struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
            new_node->data = i;
            insert_after(current_node, new_node);
        }
        player = (player+1)%num_players;
        current_node = current_node->next->next;
    }
    long int max_score = 0;
    for (int i = 0; i < num_players; ++i){
        if (scores[i] > max_score){
            max_score = scores[i];
        }
    }
    std::cout <<  max_score << std::endl;
    return 0;
}