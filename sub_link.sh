#! /bin/bash
case "${1}" in
    #提取js文件shell脚本
    subjs)
    sub_result=`./sub_server/subjs -i ./url.txt`
    echo "${sub_result}"
    ;;

    #从js文件中提取隐藏的链接shell脚本
    linkjs)
    link_result=`python3 ./LinkFinder/linkfinder.py -i $2 -o cli`
    echo "${link_result}"
    ;;

    #过滤黑名单文件
    filterbalck)
    for i in `cat ./black.txt`
        do
            cat ./dicc.txt  | grep -v ${i} > ./dicc_tmp.txt
            mv ./dicc_tmp.txt ./dicc.txt

        done
    #删除多余空行
    awk 'NF' ./dicc.txt > ./dicc1.txt
    rm -rf ./dicc.txt
    ;;

esac
