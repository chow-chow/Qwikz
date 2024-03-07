import { Button } from '@/components/ui/button'
import Image from 'next/image'
import Link from 'next/link'

export default function Home() {
	return (
		<main className='flex-1 flex'>
			<div className='container m-auto'>
				<div className='grid gap-4 sm:grid-cols-2 md:grid-cols-7 items-center'>
					<div className='col-span-3 flex flex-col items-center text-center'>
						<h1 className='scroll-m-20 text-5xl font-bold tracking-tight md:text-6xl lg:text-7xl'>
							Transform your <span className='text-primary'>classroom</span>
						</h1>
						<h4 className='scroll-m-20 text-xl md:text-2xl font-normal tracking-tight mt-6 text-foreground/60'>
							Simplify assessment and enhance learning with Qwikz.{' '}
							<span className='font-semibold text-foreground'>
								Create or take quizzes in no time
							</span>
						</h4>
						<Button size='lg' className='mt-6'>
							<Link href='/signup'>Get Started</Link>
						</Button>
					</div>
					<Image
						src={'/classroom.png'}
						width={710}
						height={532.5}
						className='col-span-4'
						alt='Classroom illustration'
					/>
				</div>
			</div>
		</main>
	)
}
