using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnManager : MonoBehaviour
{

    [SerializeField]
    private GameObject _enemyPrefab;

    [SerializeField]
    private GameObject _EnemyContainer;

    [SerializeField]
    private GameObject[] powerups;


    private bool _stopenemySpawning;

    private bool _stopPowerupSpawning;

    // Start is called before the first frame update
 

    public void StartSpawning()
    {
        StartCoroutine(SpawnEnemyRoutine());
        StartCoroutine(SpawnPowerupRoutine());
    }
    // Update is called once per frame
    void Update()
    {
        
    }

    IEnumerator SpawnEnemyRoutine()
    {
        yield return new WaitForSeconds(3.0f);
        while (_stopenemySpawning == false)
        {
            Vector3 poseToSpawn = new Vector3(Random.Range(-8f, 8f), 7, 0);
            GameObject newEnemy = Instantiate(_enemyPrefab, poseToSpawn , Quaternion.identity);
            newEnemy.transform.parent = _EnemyContainer.transform;
            yield return new WaitForSeconds(5.0f);
        }
    }

    IEnumerator SpawnPowerupRoutine()
    {
        yield return new WaitForSeconds(3.0f);
        while (_stopPowerupSpawning == false)
        {
            Vector3 poseToSpawn = new Vector3(Random.Range(-8f, 8f), 7, 0);
            int randompowerup = Random.Range(0, 3);
            Instantiate(powerups[randompowerup], poseToSpawn, Quaternion.identity);
            yield return new WaitForSeconds(Random.Range(3, 8));
        }
    }


    public void OnPlayerDeath()
    {
        _stopPowerupSpawning = true;
        _stopenemySpawning = true;
    }

}
