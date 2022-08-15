
import Layout from '../src/components/layout/Layout';
import Home from '../src/components/Home';
import axios from 'axios'

export default function Index({data}) {

  console.log("jobs", data)
  return (
    <Layout>
      <Home data = {data}/>
    </Layout>
  );
}


export async function getServerSideProps() {
  const response = await axios.get(`${process.env.API_URL}/api/jobs/`)
  const data = response.data;

  return {
    props: {
      data
    }
  }
}
