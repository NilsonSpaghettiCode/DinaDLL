#include <iostream>
#include <string>

extern "C"
{
    void testLib()
    {
        std::cout<<"Test v1.0.0"<<std::endl;
    }

    unsigned long long factorial(int n)
    {
        unsigned long long facto = 1;
        for(int i = 1; i<=n;i++)
        {
            facto = facto * i;
        }
        return facto;
    }

    void testPerformance(unsigned int n)
    {
        unsigned int var = 0;
        for(int i = 1; i<=n;i++)
        {
            var++;
        }
        std::cout << "Result C++: " << var << std::endl;
    }

        int main(int argc, char* argv[])
    {
        std::string nStr = argv[1];
        int n = std::stoi(nStr);
        std::cout<<"MAIN:"<<factorial(n)<<std::endl;
        return 0;
    }
}
