echo $1
if [[ -z $1 ]]
then
    echo "no argument"
    exit 1
fi

for id in `cat stu_id.txt`
do
    cp $1 $id.ipynb
done
