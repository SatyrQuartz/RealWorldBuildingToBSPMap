brushno=1

makecube () {
    posX=$(echo $pos | cut -f1 -d"," )
    posY=$(echo $pos | cut -f2 -d"," )
    sizeX=$(echo $size | cut -f1 -d"," )
    sizeY=$(echo $size | cut -f2 -d"," )
    checkangle=$(echo $angle | cut -c 1)
    echo Num:$brushno Pos:$posX $posY Size:$sizeX $sizeY 
    if [[ $angle != *"e-"* ]]; then
        if [ "$checkangle" != 0 ]; then
            if [ "$checkangle" != "3" ]; then
                sizeX=$(echo $size | cut -f2 -d"," )
                sizeY=$(echo $size | cut -f1 -d"," )
                echo Rotated $posX $posY Swapped.
            fi
        fi
    fi

    if [ $color = '0.00000000,0.00000000,1.0000000,0.47999999' ]; then
        echo "CorradorWall"
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 24 $posX $posY 0 CorradorWall $brushno >> out.map
        brushno=$((brushno+1))
    fi
    
    if [ $color = '0.00000000,1.0000000,0.00000000,0.47999999' ]; then
        echo "ClassroomWall"
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 24 $posX $posY 0 ClassroomWall $brushno >> out.map
        brushno=$((brushno+1))
    fi
    
    if [ $color = '0.50000000,0.00000000,1.0000000,0.47999999' ]; then
        echo "ClassroomFloor"
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 1 $posX $posY 0 ClassroomFloor $brushno >> out.map
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 1 $posX $posY 5 ClassroomTiledCeiling $brushno >> out.map
        brushno=$((brushno+1))
    fi
    
    if [ $color = '0.00000000,0.00000000,0.00000000,0.47999999' ]; then
        #ClassroomFloor for now
        echo "Door"
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 1 $posX $posY 0 ClassroomFloor $brushno >> out.map
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 1 $posX $posY 5 ClassroomTiledCeiling $brushno >> out.map
        brushno=$((brushno+1))
    fi

    if [ $color = '1.0000000,0.00000000,0.00000000,0.47999999' ]; then
        echo "UnFinishedWall"
        #wall for now
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 24 $posX $posY 0 UnFinishedWall $brushno >> out.map
        brushno=$((brushno+1))
    fi
    
    if [ $color = '1.0000000,0.00000000,1.0000000,0.47999999' ]; then
        echo "CorradorFloor"
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 1 $posX $posY 0 CorradorFloor $brushno >> out.map
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 1 $posX $posY 5 CorradorTiledCeiling $brushno >> out.map
        brushno=$((brushno+1))
    fi
    
    if [ $color = '1.0000000,0.50000000,0.00000000,0.47999999' ]; then
        echo "Window"
        #CorradorWall for now
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 24 $posX $posY 0 CorradorWall $brushno >> out.map
        brushno=$((brushno+1))
    fi
    
    if [ $color = '0.16666667,0.00000000,0.083333336,0.47999999' ]; then
        echo "CorradorBump"
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 1.7 $posX $posY 0 CorradorWall $brushno >> out.map
        brushno=$((brushno+1))
    fi
    
    if [ $color = '0.00000000,0.00000000,0.00000000,0.47999999' ]; then
        echo "Door"
        python3 ./03_conversion/cubecreate.py $sizeX $sizeY 4 $posX $posY 5.2 CorradorWall $brushno >> out.map
        brushno=$((brushno+1))
    fi
}

