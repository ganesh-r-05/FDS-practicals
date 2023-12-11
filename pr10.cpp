#include <iostream>
#include <stack>

using namespace std;

bool areParenthesesWellMatched(const string &expression) {
  stack<char> s;

  for (char ch : expression) {
    if (ch == '(' || ch == '[' || ch == '{') {
      s.push(ch);
    } else if (ch == ')' || ch == ']' || ch == '}') {
      if (s.empty()) {
        return false; // Closing parenthesis without a corresponding opening
                      // parenthesis
      }

      char top = s.top();
      s.pop();

      if ((ch == ')' && top != '(') || (ch == ']' && top != '[') ||
          (ch == '}' && top != '{')) {
        return false; // Mismatched parentheses
      }
    }
  }

  return s.empty(); // Check if there are any unmatched opening parentheses left
}

int main() {
  string expression;
  cout << "Enter an expression: ";
  getline(cin, expression);

  if (areParenthesesWellMatched(expression)) {
    cout << "Parentheses are well-matched." << endl;
  } else {
    cout << "Parentheses are not well-matched." << endl;
  }

  return 0;
}
