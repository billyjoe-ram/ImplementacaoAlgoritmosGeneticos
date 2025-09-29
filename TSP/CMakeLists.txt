cmake_minimum_required(VERSION 3.10)
project(TSP)

set(CMAKE_CXX_STANDARD 11)

find_package(Catch2 3 REQUIRED)

add_executable(TSPCpp src/main.cpp
        src/city.cpp
        src/city.h
        src/population.cpp
        src/population.h
        src/genetic.cpp
        src/genetic.h)

add_executable(tests
        tests/test_city.cpp
        tests/test_genetic.cpp
        tests/test_population.cpp
)

target_link_libraries(tests PRIVATE Catch2::Catch2WithMain)